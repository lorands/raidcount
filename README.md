# raidcount

A small command-line scorekeeper for kabaddi matches.

    raidcount new "Bengal Warriors" "Puneri Paltan"
    raidcount raid --team A --touch 2 --bonus
    raidcount score

Docs: `docs/handbook.adoc` (the handbook) and `docs/quickstart.md` (the quick start).

This is a sample project for GoOwl's docs-as-code demo video. `ci/github-actions/publish-markdown.yml`
is GoOwl's GitHub Actions example (`docs/ci-cd-examples/github-actions/`).
`ci/github-actions/docs.yml` drafts the user manual from the source with `goowl-docgen`
on every version tag; `.goowl/docgen.txt` tells the model who it writes for.
Both workflows are kept outside `.github/workflows/` so they do not run here; copy
them there to use them.

Licence: MIT (see `LICENSE`).
