import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router';

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
    RouterModule.forRoot(
      appRoutes,
      {enableTracing:false}
    )
  ],
  providers: [DataService, UserService, QuestionService],
  bootstrap: [AppComponent]
})
export class AppModule { }
