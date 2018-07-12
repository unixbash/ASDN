import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { LocalStorageService } from 'angular-2-local-storage';
import { Data } from '../../models/data';
import { DeviceService } from '../../services/device-service';
import { ServerDevice } from '../../models/device';
import { ActivityService } from '../../services/activity-service';
declare function testJs(): any;
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
  encapsulation: ViewEncapsulation.None
})

export class DashboardComponent implements OnInit {
    lineDataSource = {
        "chart": {
            "caption": "Network Activity",
            "subCaption": "Over Last week",
            "xAxisName": "Day",
            "yAxisName": "Mbps",
            "lineThickness": "2",
            "paletteColors": "#0075c2",
            "baseFontColor": "#333333",
            "baseFont": "Helvetica Neue,Arial",
            "captionFontSize": "14",
            "subcaptionFontSize": "14",
            "subcaptionFontBold": "0",
            "showBorder": "0",
            "bgColor": "#ffffff",
            "showShadow": "0",
            "canvasBgColor": "#ffffff",
            "canvasBorderAlpha": "0",
            "divlineAlpha": "100",
            "divlineColor": "#999999",
            "divlineThickness": "1",
            "divLineIsDashed": "1",
            "divLineDashLen": "1",
            "divLineGapLen": "1",
            "showXAxisLine": "1",
            "xAxisLineThickness": "1",
            "xAxisLineColor": "#999999",
            "showAlternateHGridColor": "0"
        },
        "data": []
    }
    dataSource = {
        "chart": {
        "caption": "Network Location",
        "palettecolors":"#607d8b, #8b6e60, #8b8460, #f3b49f, #7d608b",
        "showLegend": "1"
        },
        "data": []
    }
    devices: Object[];
    deviceList: ServerDevice[];

    oldConfig: String =
    `
   `;

    newConfig: String = this.oldConfig;
 
    constructor(
        private localStorageService: LocalStorageService,
        private activityService: ActivityService,
        private deviceService: DeviceService
    ) {}

    ngOnInit() {
        if(this.localStorageService.get("token") == null){
            window.location.href='http://localhost:4200/login';
        }
        this.devices = new Array();
        this.deviceList = new Array();
        this.getDevices();
        this.getActivity();
    }

    showConfig(index: number){
        this.oldConfig = this.deviceList[index].configOld;
        this.newConfig = this.deviceList[index].config;

    }

    getDevices(){
        this.deviceService.getCustomerDevice(this.localStorageService.get("user"), this.localStorageService.get("token"))
      .subscribe(
        deviceList => {
            let unsupported = 0;
            let online = 0;
            let offline = 0;
            let unconfigured = 0;
            let warning = 0;
            for(let i = 0; i < deviceList.length; i++){
                if(deviceList[i].status == "unsupported"){
                    unsupported++;
                }
                else if(deviceList[i].status == "online"){
                    this.devices.push({"name": deviceList[i].hostname + ""});
                    this.deviceList.push(deviceList[i])
                    online++;
                }
                else if(deviceList[i].status == "offline"){
                    this.devices.push({"name": deviceList[i].hostname + ""});
                    this.deviceList.push(deviceList[i])
                    offline++;
                }
                else if(deviceList[i].status == "unconfigured"){
                    this.devices.push({"name": deviceList[i].hostname + ""});
                    this.deviceList.push(deviceList[i])
                    unconfigured++;
                }
                else if(deviceList[i].status == "warning"){
                    this.devices.push({"name": deviceList[i].hostname + ""});
                    this.deviceList.push(deviceList[i])
                    warning++;
                }
                
            }
            this.dataSource.data.push( {"label": "unsupported", "value":unsupported + ""});
            this.dataSource.data.push( {"label": "online", "value":online + ""});
            this.dataSource.data.push( {"label": "offline", "value":offline + ""});
            this.dataSource.data.push( {"label": "unconfigured", "value":unconfigured + ""});
            this.dataSource.data.push( {"label": "warning", "value":warning + ""});
            console.log(this.dataSource);
            this.oldConfig = this.deviceList[0].configOld;
            this.newConfig = this.deviceList[0].config;

        });
    err => console.log(err);

    }

    getActivity(){
        this.activityService.getCustomerActivity(this.localStorageService.get("user"), this.localStorageService.get("token"))
      .subscribe(
        activity => {
            console.log(activity);
            let activityArray = activity.activity.split(",");
            for(let i = 0; i < activityArray.length; i++){
                let currentActivity = activityArray[0].split(":")
                this.lineDataSource.data.push( {"label": currentActivity[0], "value":currentActivity[1]});
            }

            console.log(this.dataSource);

        });
    err => console.log(err);

    }

}
