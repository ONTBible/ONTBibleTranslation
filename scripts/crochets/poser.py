#!/usr/bin/env python3
"""Pose les crochets git du vault — et rien de plus.

    python3 scripts/crochets/poser.py            pose ce qui manque
    python3 scripts/crochets/poser.py --dire     dit l'état, n'écrit rien

## Ce que ces crochets sont, et ce qu'ils ne sont pas

==La garde est la CI.== Elle tourne sur chaque pull request, chez tout le monde,
et c'est elle qui décide. Ces crochets ne font que l'annoncer plus tôt : ils
disent à la seconde ce que la CI dirait vingt minutes après la poussée.

==Un crochet absent ne crée donc aucun trou.== Il coûte un aller-retour de PR
rouge, pas de la sûreté. C'est la raison pour laquelle ce script ne s'installe
pas tout seul, n'est appelé par rien, et ne figure dans aucune épreuve : s'il
manquait, personne ne devrait s'en apercevoir autrement qu'en perdant du temps.

Si un jour quelque chose repose sur l'un d'eux, ==ce sera un défaut de
conception==, pas une amélioration.

## Pourquoi il faut une commande, et pourquoi git ne le fait pas

Git n'installe jamais un crochet depuis un dépôt cloné, et c'est délibéré de sa
part : un dépôt qu'on télécharge ne doit pas pouvoir exécuter du code à l'insu
de celui qui le clone. `.git/hooks` n'est donc pas versionné, et ne peut pas
l'être.

Ce script est le pont entre les deux : les crochets vivent dans le dépôt — donc
relus, discutés, corrigés par pull request comme le reste — et leur pose reste
un acte de celui qui travaille ici.

## Une pose couvre toutes les sessions

Les worktrees partagent le même dossier git. Poser ici pose pour toutes les
sessions du vault — ce qui est commode et ==demande d'être dit==, parce qu'un
crochet change le comportement du commit de six voisins qui ne l'ont pas
installé.
"""
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path


def dossier_des_crochets() -> Path:
    """Le dossier réel, même depuis un worktree.

    Dans un worktree, `.git` est un fichier qui renvoie ailleurs et les crochets
    vivent dans le dossier COMMUN. `--git-common-dir` le donne ; `--git-dir`
    donnerait celui du worktree, où git ne cherche pas.
    """
    commun = subprocess.run(["git", "rev-parse", "--git-common-dir"],
                            capture_output=True, text=True, check=True).stdout.strip()
    return (Path.cwd() / commun).resolve() / "hooks"


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()[:12] if chemin.exists() else "—"


def main() -> int:
    dire = "--dire" in sys.argv
    source = Path(__file__).resolve().parent
    cible = dossier_des_crochets()
    cible.mkdir(parents=True, exist_ok=True)

    crochets = sorted(p for p in source.iterdir()
                      if p.is_file() and p.name not in ("poser.py",) and not p.name.endswith(".md"))
    if not crochets:
        print("  aucun crochet à poser")
        return 0

    print(f"  crochets du dépôt : {source}")
    print(f"  dossier git       : {cible}\n")
    poses = 0
    for c in crochets:
        pose = cible / c.name
        a, b = empreinte(c), empreinte(pose)
        if a == b:
            etat = "déjà posé"
        elif not pose.exists():
            etat = "ABSENT" if dire else "posé"
        else:
            # On ne remplace pas en silence : un crochet local peut avoir été
            # modifié exprès, et l'écraser ferait disparaître un travail sans
            # que rien ne le dise.
            etat = "DIVERGENT — non touché, à comparer à la main"
        if not dire and a != b and not pose.exists():
            shutil.copy2(c, pose)
            pose.chmod(0o755)
            poses += 1
        print(f"     {c.name:<14} dépôt {a:<14} posé {b:<14} {etat}")

    if dire:
        print("\n  (--dire : rien n'a été écrit)")
    else:
        print(f"\n  {poses} posé(s). La garde reste la CI ; ceci ne fait que l'anticiper.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
