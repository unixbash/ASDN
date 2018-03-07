import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { QuestionService } from './services/question.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers:  [QuestionService]
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

export class AppComponent {
  questions: any[];

  constructor(service: QuestionService) {
    this.questions = service.getQuestions();
  }
}
