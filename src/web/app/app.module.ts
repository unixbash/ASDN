import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { UserComponent } from './components/user/user.component';
import { NetworkComponent } from './components/network/network.component';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';

import { DataService } from './services/data.service';
import { AccountComponent } from './components/account/account.component';
import { componentFactoryName } from '@angular/compiler';
import { Component } from '@angular/core/src/metadata/directives';
import { LoadedRouterConfig } from '@angular/router/src/config';

import { AlertModule } from 'ngx-bootstrap';

const appRoutes:Routes = [
  {path:'', component:UserComponent},
  {path:'dashboard', component:DashboardComponent, data: { title: 'ASDN - Dashboard' }},
  {path:'account', component:AccountComponent, data: { title: 'ASDN - Account' }},
  {path:'login', component:LoginComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    NetworkComponent,
    LoginComponent,
    DashboardComponent,
    AccountComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
      {
        path:'',
        component: LoginComponent
      },
      {
      path:'dashboard',
      component: DashboardComponent
      }
    ])
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
