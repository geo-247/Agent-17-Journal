why does the vault service restart every day at exactly 04:17?
checked crontab - nothing there
checked systemd timers - nothing matching 04:17
system logs show clean SIGTERM received from PID 1.
did IT set up an external healthcheck that reboots unprompted?
need to check with Marcus or just let it go.
probably just automated fleet maintenance.
fatigue is getting to me.
coffee machine on floor 2 broken again.
