
## Set SSH Keepalive 

SSH connection can be dropped at times, but it shouldn’t be too frequent. 
One thing you can do in the client side is to change the keep alive settings globally. You can do that by editing `~/.ssh/config`

```bash
Host *
  ServerAliveInterval 240
  ServerAliveCountMax 4
```

## Using Spot Instance

```
% grid session create --use_spot --instance_type t2.medium   
✔ Creating Interactive node ...

                Interactive node created!

                `grid status` to list all runs and interactive nodes.
                `grid status misty-vulture-372` to see the status for this interactive node.

                ----------------------
                Submission summary
                ----------------------
                name:                    misty-vulture-372
                instance_type:           t2.medium
                cloud_provider:          aws
                cloud_credentials:       cc-qdfdk
                datastore_name:          None
                datastore_version:       None
                datastore_mount_dir:     None
                use_spot:                True
                
Interactive node misty-vulture-372 is spinning up.
```


```
% grid session create --use_spot --instance_type g4dn.2xlarge
✔ Creating Interactive node ...

                Interactive node created!

                `grid status` to list all runs and interactive nodes.
                `grid status knowing-agouti-716` to see the status for this interactive node.

                ----------------------
                Submission summary
                ----------------------
                name:                    knowing-agouti-716
                instance_type:           g4dn.2xlarge
                cloud_provider:          aws
                cloud_credentials:       cc-qdfdk
                datastore_name:          None
                datastore_version:       None
                datastore_mount_dir:     None
                use_spot:                True
                
Interactive node knowing-agouti-716 is spinning up.
```
