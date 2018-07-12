export interface VPN1{
    publicAddress: string;
    privateAddress: string;
    ikeAA: string;
    ipsecEA: string;
    dh: string;
    ikeLife: string;
    ikeSecret: string;
    ikeVer: string;
}

export interface VPN2{
    ikeAuth: string;
    ipsecAuth: string;
    ipsecLife: string;
    ipsecPFS: string;
}

export class VPN{
    id: string;
    customerId: string;
    publicIp: string;
    privateSubnet: string;
    ikeAl: string;
    ipsecEnc: string;
    dhGroup: string;
    ikeLife: string;
    ikeSecret: string;
    ikeVersion: string;
    ikeAuth: string;
    ipsecAl: string;
    ipsecLife: string;
    ipsecSecret: string;
}