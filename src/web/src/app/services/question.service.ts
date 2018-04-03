import { Injectable }       from '@angular/core';

import { DropdownQuestion } from '../question-dropdown';
import { QuestionBase }     from '../question-base';
import { TextboxQuestion }  from '../question-textbox';

@Injectable()
export class QuestionService {

  // Todo: get from a remote source of question metadata
  // Todo: make asynchronous
  getQuestions() {

    let questions: QuestionBase<any>[] = [

      new TextboxQuestion({
        key: 'caseTitle',
        label: 'Case Title',
        value: '',
        order: 1
      }),

      new DropdownQuestion({
        key: 'severity',
        label: 'Severity',
        options: [
          {key: 'l1',  value: 'Level 1 - Critical Production Impact'},
          {key: 'l2',  value: 'Level 2 - High Production Impact'},
          {key: 'l3',  value: 'Level 3 - Internal Development Impact'},
          {key: 'l4',  value: 'Level 4 - Low/No Operational Impact'}
        ],
        order: 2
      }),

      new TextboxQuestion({
        key: 'Description',
        label: 'Description',
        order: 3
      }),

      

    ];

    return questions.sort((a, b) => a.order - b.order);
  }
}