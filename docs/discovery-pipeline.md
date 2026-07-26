# Discovery Pipeline

## Objective

Execute a deterministic sequence of reconnaissance stages against an authorized target, persist optional raw stage outputs, and normalize results into a stable schema for evidence and reporting.

## Orchestrator

`DiscoveryOrchestrator` (`src/recon/discovery/orchestrator.py`) owns stage ordering.

```text
DNS → Probe → Service → TLS → Line Protocol → Virtual Host
  → Authentication → Authenticated HTTP → Fingerprint → Normalize
```

## Stage Contracts

| Stage | Inputs | Typical outputs |
|-------|--------|-----------------|
| DNS | Target host | Hostname, addresses, records |
| Probe | Target URL/host | Reachability, HTTP metadata |
| Service | Target | Open ports / service table |
| TLS | Target | Certificate / protocol summary |
| Line protocol | Target | Banner / capability signals |
| Virtual host | Arguments + line protocol | Candidate vhosts |
| Authentication | Arguments + vhost + line protocol | Auth success / failure |
| Authenticated HTTP | Arguments + authentication | Protected resource retrieval |
| Fingerprint | Arguments + virtual hosts | Technology indicators |
| Normalize | Aggregated stage dict | Canonical section schema |

## Raw Output Persistence

When enabled by the orchestrator integration, `RawOutputWriter` stores per-stage JSON under:

```text
output/raw-output/<stage>.json
```

Raw files are intermediate evidence of tool results prior to normalization.

## Normalization Rules

`Normalizer` always returns these keys:

- `dns`
- `probe`
- `services`
- `tls`
- `line_protocol`
- `virtual_hosts`
- `authentication`
- `authenticated_http`
- `fingerprint`

Missing stages become empty dictionaries. Present stages are preserved without transformation beyond key selection.

## Failure Semantics

Individual stages may return structured failure reasons (for example, authentication unsuccessful when no virtual host was discovered). Downstream stages and writers are designed to tolerate empty or unsuccessful sections rather than aborting the entire assessment unnecessarily.

## Operator Notes

- Prefer `--assignment` in lab environments so host/port/profile values remain consistent with the authorized runtime.
- Do not reorder stages casually; later stages depend on earlier outputs.
- Discovery logic is assessment-frozen for portfolio packaging—document changes carefully if extending.

## Related Documents

- [Architecture](architecture.md)
- [Evidence pipeline](evidence-pipeline.md)
- [Extension guide](extension-guide.md)
