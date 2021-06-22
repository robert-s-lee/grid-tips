These are step by step instructions to troubleshoot Grid.ai CLI.

- [Check Environment](#check-environment)
- [Check Grid Access](#check-grid-access)
- [Recovery Steps](#recovery-steps)

# Check Environment

The the following command to verify [Grid.ai CLI](https://docs.grid.ai/products/global-cli-configs).

```bash
which grid
pip show lightning-grid
grid version
```
Details to the above commands are below:

- Verify the path of `grid`.  In this example, `kd` is Conda environment name.
```bash
 % which grid
/opt/miniconda3/envs/kd/bin/grid
```

- Verify the version of the `lightning-grid` module.  In this example, `0.3.73` is the version name.
```bash
% pip show lightning-grid
Name: lightning-grid
Version: 0.3.73
Summary: Grid Python SDK.
Home-page: https://grid.ai
Author: Grid AI Engineering
Author-email: grid-eng@grid.ai
License: UNKNOWN
Location: /opt/miniconda3/envs/kd/lib/python3.7/site-packages
Requires: ...
Required-by:
```

- Verify the `grid` show the matching version.

```bash
% grid version
                                Grid CLI (v0.3.73)
                               https://docs.grid.ai
```



# Check Grid Access

The the following command to verify Grid.ai access.

```bash
grid login
grid clusters
grid status
```

Details to the above commands are below:

- Verify [`grid login`](https://docs.grid.ai/products/global-cli-configs/cli-api/grid-login) using API Keys from [https://platform.grid.ai/#/settings?tabId=apikey](https://platform.grid.ai/#/settings?tabId=apikey)

```bash
grid login
```

Verify [`grid clusters`](https://docs.grid.ai/platform/about-these-features/adding-custom-cloud-credentials) show Grid.ai clusters in running state.

```bash
% grid clusters
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ id                  ┃ name                ┃ status  ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ grid-cloud-prod     │ grid-cloud-prod     │ running │
└─────────────────────┴─────────────────────┴─────────┘
```

Verify [`grid status`](https://docs.grid.ai/products/global-cli-configs/cli-api/grid-status) show expected Grid.ai `run` and `sessions`.

```bash
% grid status
✔ Done!
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┓
┃ Run          ┃ Project ┃ Status ┃ Duration ┃ Experiments ┃ Running ┃ Queued ┃ Completed ┃ Failed ┃ Stopped ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━┩
│ None Active. │         │        │          │             │         │        │           │        │         │
└──────────────┴─────────┴────────┴──────────┴─────────────┴─────────┴────────┴───────────┴────────┴─────────┘

62 Run(s) are not active. Use `grid history` to view your Run history.
┏━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━┓
┃ Name         ┃ Status ┃ Instance Type ┃ Duration ┃ URL ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━┩
│ None Active. │        │               │          │     │
└──────────────┴────────┴───────────────┴──────────┴─────┘
```

# Recovery Steps

- Try uninstall and re-install of Grid.ai CLI and retry the troubleshooting steps.
```bash
pip uninstall lightning-grid
pip install lightning-grid --upgrade
```

- Try remove and re-activate conda environment and retry the troubleshooting steps.
'''bash
conda activate base
conda env remove --name kd
conda create --name kd python=3.7
conda activate kd
```