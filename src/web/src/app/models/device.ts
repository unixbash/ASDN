export class DevicesStatusToken {
    status:[string];
}

export class ServerDevice {

    id: string;
    createdAt: string;
    updatedAt: string;
    customerId: string;
    hostname: string;
    address: string;
    vendor: string;
    status: string;
    config: string;
    configOld: string;
    latestos: string;
}

export class Lan{
    id: string;
    createdAt: string;
    updatedAt: string;
    deviceId: string;
    name: string;
    tag: string;
    interfaces: string;
    qos: string;
}

export class Interface{
    id: string;
    createdAt: string;
    updatedAt: string;
    deviceId: string;
    interfaces: string;
}

export class Service{
    id: string;
    createdAt: string;
    updatedAt: string;
    deviceId: string;
    name: string;
    traversing: string;
    source: string;
    destination: string;
    application: string;
    action: string;
}

export class Routing{
    id: string;
    createdAt: string;
    updatedAt: string;
    deviceId: string;
    source: string;
    destination: string;
    interfaces: string;
    type: string;
}

export class ServerActivity {
    id: string;
    createdAt: string;
    updatedAt: string;
    customerId: string;
    activity: string;
}

export class Device {
    id = "1";
    name: "SRX1500";

    states = new Map([
        ["inactive","/assets/port-inactive.png"],
        ["ok","/assets/port-ok.png"],
        ["alert","/assets/port-alert.png"],
        ["error","/assets/port-error.png"]
    ]);

    interfaces: { name:string, portStatus:string, portImg:string } [] = [
        {"name":"ge-0/0/0", "portStatus":"Inactive", "portImg":this.states.get("inactive")},
        {"name":"ge-0/0/1", "portStatus":"", "portImg":this.states.get("ok")},
        {"name":"ge-0/0/2", "portStatus":"Alert", "portImg":this.states.get("alert")},
        {"name":"ge-0/0/3", "portStatus":"Error", "portImg":this.states.get("error")},
        {"name":"ge-0/0/4", "portStatus":"", "portImg":this.states.get("ok")},
        {"name":"ge-0/0/5", "portStatus":"", "portImg":this.states.get("ok")},
        {"name":"ge-0/0/6", "portStatus":"Alert", "portImg":this.states.get("alert")},
        {"name":"ge-0/0/7", "portStatus":"Alert","portImg":this.states.get("alert")},
        {"name":"ge-0/0/8", "portStatus":"", "portImg":this.states.get("ok")},
        {"name":"ge-0/0/9", "portStatus":"", "portImg":this.states.get("ok")},
        {"name":"ge-0/0/10", "portStatus":"Inactive", "portImg":this.states.get("inactive")},
        {"name":"ge-0/0/11", "portStatus":"Inactive", "portImg":this.states.get("inactive")},
        {"name":"ge-0/0/12", "portStatus":"Inactive", "portImg":this.states.get("inactive")},
        {"name":"ge-0/0/13", "portStatus":"Inactive", "portImg":this.states.get("inactive")},
        {"name":"ge-0/0/14", "portStatus":"", "portImg":this.states.get("ok")},
        {"name":"ge-0/0/15", "portStatus":"", "portImg":this.states.get("ok")},
    ];   
    
    routeInfo: { source:string, destination:string, interfaces:string, type:string } [] = [
        {"source":"0.0.0.0/0", "destination":"10.10.10.1", "interfaces":"ge-0/0/5.0", "type":"Static"},
        {"source":"10.10.10.0/24", "destination":"10.10.10.0/24", "interfaces":"ge-0/0/5.0", "type":"Direct"},
        {"source":"10.10.10.110/32", "destination":"10.10.10.110/32", "interfaces":"ge-0/0/5.0", "type":"Local"}
    ];

    vlanInfo: { name:string, tag:string, interfaces:string, qos:string } [] = [
        {"name":"VoIP", "tag":"110", "interfaces":"ge-0/0/0.0", "qos":"Yes"},
        {"name":"Data", "tag":"100", "interfaces":"ge-0/0/0.0", "qos":"No"},
        {"name":"CCTV", "tag":"90", "interfaces":"ge-0/0/0.0", "qos":"No"}
    ];

    securityInfo: { name:string, traversing:string, srcAddress:string, dstAddress:string, application:string, action:string } [] = [
        {"name":"allow-web", "traversing":"untrust to trust", "srcAddress":"any", "dstAddress":"web-server", "application":"junos-https", "action":"allow"},
        {"name":"allow-ftp", "traversing":"untrust to trust", "srcAddress":"any", "dstAddress":"ftp-server", "application":"junos-ftp", "action":"allow, log"},
        {"name":"allow-users", "traversing":"trust to untrust", "srcAddress":"net_10", "dstAddress":"any", "application":"any", "action":"allow"},
        {"name":"allow-vpn", "traversing":"untrust to vpn", "srcAddress":"any", "dstAddress":"any", "application":"any", "action":"allow, log"},
        {"name":"deny-all", "traversing":"untrust to trust", "srcAddress":"any", "dstAddress":"any", "application":"any", "action":"deny, log"},
    ];
}