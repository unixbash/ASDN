import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';
import {LocalStorageModule} from 'angular-2-local-storage';
// Import angular2-fusioncharts
import { FusionChartsModule } from 'angular2-fusioncharts';

// Import FusionCharts library and chart modules
import * as FusionCharts from 'fusioncharts';
import * as Charts from 'fusioncharts/fusioncharts.charts';
import * as FintTheme from 'fusioncharts/themes/fusioncharts.theme.fint';

import { AppComponent } from './app.component';
import { UserComponent } from './components/user/user.component';
import { NetworkComponent } from './components/network/network.component';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';

import { DataService } from './services/data.service';
import { componentFactoryName } from '@angular/compiler';
import { Component } from '@angular/core/src/metadata/directives';
import { LoadedRouterConfig } from '@angular/router/src/config';

import { UserService } from './services/user-service';
import { NavComponent } from './components/nav/nav.component';
import { HelpComponent } from './components/help/help.component';
import { SettingsComponent } from './components/settings/settings.component';
import { WizzardComponent } from './components/wizzard/wizzard.component';
import { QuestionService } from './services/question.service';
import { DynamicFormComponent } from './components/dynamic-form/dynamic-form.component';
import { DynamicFormQuestionComponent } from './components/dynamic-form-question/dynamic-form-question.component';
import { VpnService } from './services/vpn-service';
import { DeviceService } from './services/device-service';
import { ActivityService } from './services/activity-service';

const appRoutes:Routes = [
  {path:'', redirectTo:'/login', pathMatch:'full'},
  {path:'login', component:LoginComponent, data: { title: 'ASDN - Login' }},
  {path:'dashboard', component:DashboardComponent, data: { title: 'ASDN - Dashboard' }},
  {path:'wizzard', component:DashboardComponent, data: { title: 'ASDN - Wizzard' }},
  {path:'network', component:NetworkComponent, data: { title: 'ASDN - Network' }},
  {path:'help', component:HelpComponent, data: { title: 'ASDN - Help' }},
  {path:'settings', component:SettingsComponent, data: { title: 'ASDN - Settings' }},
  {path:'forms', component:DynamicFormQuestionComponent, data: { title: 'ASDN - Forms' }}
];

// Pass the fusioncharts library and chart modules
FusionChartsModule.fcRoot(FusionCharts, Charts, FintTheme);

@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    NetworkComponent,
    LoginComponent,
    DashboardComponent,
    NavComponent,
    HelpComponent,
    SettingsComponent,
    WizzardComponent,
    DynamicFormQuestionComponent,
    DynamicFormComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    ReactiveFormsModule,
    HttpClientModule,
    FusionChartsModule,
    RouterModule.forRoot(
      appRoutes,
      {enableTracing:false}
    ),
    LocalStorageModule.withConfig({
      prefix: 'asdn',
      storageType: 'localStorage'
  })

  ],
  providers: [DataService, UserService, QuestionService, VpnService, DeviceService, ActivityService], 
  bootstrap: [AppComponent]
})
export class AppModule { }
