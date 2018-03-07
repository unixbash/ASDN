import { Component, OnInit, ViewEncapsulation, Input } from '@angular/core';
import { FormGroup } from '@angular/forms';

import { QuestionBase }               from '../../question-base';
import { QuestionControlService }     from '../../question-control.service'
import { QuestionService }            from '../../services/question.service';

@Component({
  selector: 'app-help',
  templateUrl: './help.component.html',
  styleUrls: ['./help.component.css'],
  providers: [ QuestionControlService ],
  encapsulation: ViewEncapsulation.None
})
export class HelpComponent {

  questions: any[];

  constructor(service: QuestionService) {
    this.questions = service.getQuestions();
  }

}