import { FormGroup, FormControl, Validators } from '@angular/forms';
import { AuthService } from 'src/app/http-services/auth.service';
import { Component, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Title } from '@angular/platform-browser';
import { TypeRegisterForm } from 'src/app/models/auth';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['../../../assets/styles/form.scss']
})
export class RegisterComponent implements OnInit {
  form = new FormGroup({
    username: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required]),
    password2: new FormControl('', [Validators.required])
  })

  error = new BehaviorSubject<string>('');

  register(event: Event): void{
    event.preventDefault();
    if (this.form.valid){
      const username = this.form.get("username")?.value;
      const password = this.form.get("password")?.value;
      const password2 = this.form.get("password2")?.value;

      if (password !== password2){
        this.error.next("пароли не совпадают");
        return;
      }
      this.error.next("");

      if (username !== null && username !== undefined && password !== null && password !== undefined){
        const data: TypeRegisterForm = {
          username: username,
          password: password
        }

        this.authService.register(data, this.error);
      }
    }
  }

  constructor(
    public authService: AuthService,
    private titleService: Title
  ) {
    this.titleService.setTitle("Регистрация")
  }

  ngOnInit(): void {
  }
}
