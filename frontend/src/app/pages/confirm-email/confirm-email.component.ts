import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/http-services/auth.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { TypePayload } from 'src/app/models/auth';

@Component({
  selector: 'app-confirm-email',
  templateUrl: './confirm-email.component.html',
  styleUrls: ['../../../assets/styles/form.scss']
})
export class ConfirmEmailComponent implements OnInit {
  code: string = "";
  error: string = "";
  incorrectCodeError: string = "";
  payload: TypePayload;

  constructor(
    private authService: AuthService,
    private route: ActivatedRoute,
    private router: Router
  ) {
  }

  form = new FormGroup({
    code: new FormControl('', [Validators.required, Validators.maxLength(6), Validators.minLength(6)]),
  });

  checkVerificationCode(event: Event){
    event.preventDefault();

    if (this.payload.code === String(this.form.get('code')?.value)){
        this.incorrectCodeError = "";
        this.authService.activateUser(this.payload.user_id);
    }
    else{
      this.incorrectCodeError = "Неправильный код"
    }
  }

  ngOnInit(): void {
    this.route.params.subscribe(async params => {
      const token = params['token'];

      const payload = await this.authService.getConfirmEmailPayload(token);
      if (!payload){
        this.error = "Неверный url адресс"
      }
      else{
        this.payload = payload;
      }
    })
  }
}
