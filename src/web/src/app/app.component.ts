import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

@Component({
  selector: 'app-nav',
  templateUrl: './components/nav/nav.component.html',
  styleUrls: ['./components/nav/nav.component.css']
})

@Component({
  selector: 'app-wizzard',
  templateUrl: './components/wizzard/wizzard.component.html',
  styleUrls: ['./components/wizzard/wizzard.component.css']
})

export class AppComponent {}
