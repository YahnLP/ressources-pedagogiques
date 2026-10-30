"""À lancer depuis la racine de ressources-pedagogiques après extraction du ZIP."""
from pathlib import Path
p=Path('BAC PRO CIEL/E2')
if not p.is_dir():
 raise SystemExit('Exécuter depuis la racine du dépôt GitHub.')
corrections={'./01-images/cms.png':'./01-images/CMS.png','./03-images/v.png':'./03-images/V.png'}
count=0
for md in p.glob('*.md'):
 before=md.read_text(encoding='utf-8')
 after=before
 for old,new in corrections.items():after=after.replace(old,new)
 if after!=before:md.write_text(after,encoding='utf-8');count+=1;print('Corrigé :',md)
print('Nombre de fichiers de cours corrigés :',count)
print('Le dossier images est maintenant complété avec les nouvelles illustrations.')
