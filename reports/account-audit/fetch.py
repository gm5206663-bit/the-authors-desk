import json, urllib.request, urllib.error, os, time
TOK=open('/tmp/.ght').read().strip()
H={'Authorization':f'Bearer {TOK}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
def api(path, method='GET'):
    url = path if path.startswith('http') else 'https://api.github.com'+path
    for attempt in range(3):
        try:
            req=urllib.request.Request(url, headers=H, method=method)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode() or '{}'), dict(r.headers)
        except urllib.error.HTTPError as e:
            if e.code in (403,429) and attempt<2:
                time.sleep(3); continue
            return {'__error__': e.code, '__msg__': e.read().decode()[:200]}, {}
        except Exception as e:
            if attempt<2: time.sleep(2); continue
            return {'__error__': 'exc', '__msg__': str(e)[:200]}, {}
    return {}, {}

USER='gm5206663-bit'
repos=[r['name'] for r in json.load(open('/tmp/repos.json'))]
out={}
for name in repos:
    print('scanning', name, flush=True)
    d={}
    r,_=api(f'/repos/{USER}/{name}'); d['repo']=r
    br,_=api(f'/repos/{USER}/{name}/branches?per_page=100'); d['branches']=br
    prs,_=api(f'/repos/{USER}/{name}/pulls?state=open&per_page=100'); d['open_prs']=prs if isinstance(prs,list) else []
    prs_closed,_=api(f'/repos/{USER}/{name}/pulls?state=closed&per_page=100'); d['closed_prs']=prs_closed if isinstance(prs_closed,list) else []
    iss,_=api(f'/repos/{USER}/{name}/issues?state=open&per_page=100'); d['open_issues']=iss if isinstance(iss,list) else []
    rel,_=api(f'/repos/{USER}/{name}/releases?per_page=20'); d['releases']=rel if isinstance(rel,list) else []
    tags,_=api(f'/repos/{USER}/{name}/tags?per_page=20'); d['tags']=tags if isinstance(tags,list) else []
    runs,_=api(f'/repos/{USER}/{name}/actions/runs?per_page=10'); d['actions']=runs if isinstance(runs,dict) else {}
    try:
        t=urllib.request.Request(f'https://api.github.com/repos/{USER}/{name}/contents/.github/workflows', headers=H)
        with urllib.request.urlopen(t,timeout=20) as r_: d['workflows']=[f['name'] for f in json.loads(r_.read().decode())]
    except Exception: d['workflows']=[]
    try:
        t=urllib.request.Request(f'https://api.github.com/repos/{USER}/{name}/contents/', headers=H)
        with urllib.request.urlopen(t,timeout=20) as r_: d['root_files']=[(f['name'],f['type'],f.get('size',0)) for f in json.loads(r_.read().decode())]
    except Exception: d['root_files']=[]
    langs,_=api(f'/repos/{USER}/{name}/languages'); d['languages']=langs
    con,_=api(f'/repos/{USER}/{name}/contributors?per_page=10'); d['contributors']=con if isinstance(con,list) else []
    out[name]=d
json.dump(out, open('/home/user/github-audit/audit.json','w'), indent=1)
print('\nDONE ->', len(out), 'repos')
