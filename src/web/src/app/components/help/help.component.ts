import { Component, OnInit, ViewEncapsulation, Input } from '@angular/core';
import { FormGroup } from '@angular/forms';

import { QuestionBase }               from '../../question-base';
import { QuestionControlService }     from '../../question-control.service'
import { QuestionService }            from '../../services/question.service';
import { LocalStorageService } from 'angular-2-local-storage';

@Component({
  selector: 'app-help',
  templateUrl: './help.component.html',
  styleUrls: ['./help.component.css'],
  providers: [ QuestionControlService ],
  encapsulation: ViewEncapsulation.None
})
export class HelpComponent implements OnInit {

  questions: any[];

  constructor(
    private localStorageService: LocalStorageService,
    service: QuestionService
  ) {
    this.questions = service.getQuestions();
  }

  ngOnInit(): void {
    if(this.localStorageService.get("token") == null){
      window.location.href='http://localhost:4200/login';
  }
  }

}