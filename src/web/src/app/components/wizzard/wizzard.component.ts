import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-wizzard',
  templateUrl: './wizzard.component.html',
  styleUrls: ['./wizzard.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class WizzardComponent {

  rForm: FormGroup;
  post: any;
  publicAddress:string = '';
  privateAddress:string = '';

  constructor(private fb: FormBuilder) {
    this.rForm = fb.group({
      'publicAddress' : [null, Validators.required],
      'privateAddress' : [null, Validators.compose(
        [Validators.required, Validators.minLength(7), Validators.maxLength(15)])],
    })
  }

  addPost(post) {
    this.publicAddress = post.publicAddress;
    this.privateAddress = post.privateAddress;
  }

}
