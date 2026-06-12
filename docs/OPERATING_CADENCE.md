# Operating Cadence

This registry should improve through repeated PDCA loops.

## Weekly Radar

Every week:

- scan selected GitHub topics and repos
- update metadata for active candidates
- add new candidates only when they match a node capability
- mark stale candidates for review

## Reference Inspector Rhythm

For fixed architecture reference projects, run every Monday and Thursday:

```text
Monday -> Thursday -> Monday
```

This gives a 3-4 day rhythm.

Run:

```bash
python3 scripts/validate_inspectors.py
python3 scripts/run_reference_inspection.py
```

Then the chief inspector should decide whether external updates deserve:

- no action
- watch
- document pattern
- update node design
- update rail design
- propose compound pattern
- propose taxonomy change

The chief inspector proposes. The user decides.

## Monthly Review

Every month:

- choose one node capability family
- move top candidates from metadata triage to docs review
- create at least one reproducible test fixture
- update score and risk notes

## Quarterly Sediment

Every quarter:

- promote proven candidates to approved for specific use cases
- create reusable adapters, skills, or templates
- archive deprecated or weak candidates
- update Super SOP Node OS references if taxonomy changes

## PDCA Loop

| Phase | Action |
|---|---|
| Plan | Choose node family and evaluation question. |
| Do | Scan, normalize, review, test. |
| Check | Score and compare against evidence. |
| Act | Approve, reject, defer, or sediment adapter. |
