import { Component, OnInit, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
  encapsulation: ViewEncapsulation.None
})

export class DashboardComponent implements OnInit {
  
  devices: Object[] = [
    {"name":"EX2200"},
    {"name":"SRX1500"},
    {"name":"SRX640"},
    {"name":"EX4600"},
    {"name":"SRX240"},
    {"name":"SRX640"},
    {"name":"SRX4600"},
    {"name":"SRX240"},
    {"name":"SRX640"},
    {"name":"QFX5100"},
    {"name":"ACX2200"}
  ];

  oldConfig: String =
  `
  ## Last commit: 2018-05-02 14:57:11 IST by asdn
  system {
    host-name SRX210;
    time-zone America/New_York;
    root-authentication {
        encrypted-password "$1$9kBlrO.i$zyroxBDDGRBAYu4Pap27k0"; ## SECRET-DATA
    }
    name-server {
        208.67.222.222;
        208.67.220.220;
    }
    login {
        user eric {
            uid 2002;
            class super-user;
            authentication {
                encrypted-password "$1$gQkHMOTL$UDXH432yZIKKlw6P8Qtzo."; ## SECRET-DATA
            }
        }
    }
    services {
        ssh;
        telnet;
        web-management {
            http {
                interface vlan.0;
            }
            https {
                system-generated-certificate;
                interface vlan.0;
            }
        }
        dhcp {
            router {
                192.168.1.1;
            }
            pool 192.168.1.0/24 {
                address-range low 192.168.1.10 high 192.168.1.99;
            }
            propagate-settings fe-0/0/7;
        }
    }
    syslog {
        archive size 100k files 3;
        user * {
            any emergency;
        }
        file messages {
            any critical;
            authorization info;
        }
        file interactive-commands {
            interactive-commands error;
        }
    }
    max-configurations-on-flash 5;
    max-configuration-rollbacks 5;
    license {
        autoupdate {
            url https://ae1.juniper.net/junos/key_retrieval;
        }
    }
}
interfaces {
    interface-range interfaces-trust {
        member ge-0/0/0;
        member ge-0/0/1;
        member fe-0/0/2;
        member fe-0/0/3;
        member fe-0/0/4;
        member fe-0/0/5;
        member fe-0/0/6;
        unit 0 {
            family ethernet-switching {
                vlan {
                    members vlan-trust;
                }
            }
        }
    }
    fe-0/0/7 {
        unit 0 {
            family inet {
                dhcp;
            }
        }
    }
    vlan {
        unit 0 {
            family inet {
                address 192.168.1.1/24;
            }
        }
    }
}
security {
    nat {
        source {
            rule-set trust-to-untrust {
                from zone trust;
                to zone untrust;
                rule source-nat-rule {
                    match {
                        source-address 0.0.0.0/0;
                    }
                    then {
                        source-nat {
                            interface;
                        }
                    }
                }
            }
        }
    }
    screen {
        ids-option untrust-screen {
            icmp {
                ping-death;
            }
            ip {
                source-route-option;
                tear-drop;
            }
            tcp {
                syn-flood {
                    alarm-threshold 1024;
                    attack-threshold 200;
                    source-threshold 1024;
                    destination-threshold 2048;
                    timeout 20;
                }
                land;
            }
        }
    }
    zones {
        security-zone trust {
            host-inbound-traffic {
                system-services {
                    all;
                }
                protocols {
                    all;
                }
            }
            interfaces {
                vlan.0;
            }
        }
        security-zone untrust {
            screen untrust-screen;
            interfaces {
                ge-0/0/0.0 {
                    host-inbound-traffic {
                        system-services {
                            dhcp;
                            tftp;
                        }
                    }
                }
            }
        }
    }
    policies {
        from-zone trust to-zone untrust {
            policy trust-to-untrust {
                match {
                    source-address any;
                    destination-address any;
                    application any;
                }
                then {
                    permit;
                }
            }
        }
    }
}
poe {
    interface all;
}
vlans {
    vlan-trust {
        vlan-id 3;
        l3-interface vlan.0;
    }
}`;

newConfig: String = this.oldConfig;

    

  constructor() {}

  ngOnInit() {
    
  }

}
