# Sync with infra team - Sep 19

- Jenkins pipeline still timing out on arm64 runners
- Storage quota for cluster 3 increased to 4TB
- Dave mentioned OpenVault schema migration scheduled for next Tuesday night (02:00 UTC)
- Remind Sarah about the SSL certificate expiry on api.internal
- Lunch with Dev team on Friday?
- Questions:
  * Why was table `vault_audit_events` truncated on the 16th?
  * Nobody admitted doing it. Need to ask Henderson.
  * DB replication lag is ~400ms during peak hours
- TODO:
  - [ ] re-run migration dry-run
  - [ ] submit timesheet before 5pm
