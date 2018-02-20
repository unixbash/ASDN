import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';
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
import { UserService } from './services/user-service';
import { NavComponent } from './components/nav/nav.component';

const appRoutes:Routes = [
  {path:'', redirectTo:'/login', pathMatch:'full'},
  {path:'login', component:LoginComponent, data: { title: 'ASDN - Login' }},
  {path:'dashboard', component:DashboardComponent, data: { title: 'ASDN - Dashboard' }},
  {path:'account', component:AccountComponent, data: { title: 'ASDN - Account' }}
];

@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    NetworkComponent,
    LoginComponent,
    DashboardComponent,
    AccountComponent,
    NavComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
      {enableTracing:true}
    )
  ],
  providers: [DataService, UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
