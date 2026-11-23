from pathlib import Path
import json

root = Path(__file__).parent
items = json.loads((root/'games.json').read_text(encoding='utf-8'))
assert len(items) >= 10
assert len({q['id'] for q in items}) == len(items)
assert all(sum(q['difficulty'] == level for q in items) >= n for level, n in [('kolay',4),('orta',4),('zor',2)])
for q in items:
    assert all(q.get(k) for k in ('id','name','difficulty','genre','hint','fact'))
    assert len(q['icons']) == 3 and len(q['distractors']) == 3
    assert len(set(q['distractors'])) == 3 and q['name'] not in q['distractors']
    assert q['difficulty'] in ('kolay','orta','zor')
template = (root/'index.template.html').read_text(encoding='utf-8')
assert template.count('__GAME_DATA__') == 1
payload = json.dumps(items,ensure_ascii=False,separators=(',',':')).replace('</','<' + chr(92) + '/')
html = template.replace('__GAME_DATA__',payload)
(root/'index.html').write_text(html,encoding='utf-8')
print(f'Generated {len(items)} questions into index.html')
