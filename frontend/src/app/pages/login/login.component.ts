import { FormGroup, FormControl, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { Title } from '@angular/platform-browser';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['../../../assets/styles/form.scss']
})
export class LoginComponent implements OnInit {
  error = new BehaviorSubject<string>('');

  getAccessToken(event: Event): void{
    event.preventDefault();
    if (this.form.valid){
      const formData = new FormData();
      const username = this.form.get('username')?.value;
      const password = this.form.get('password')?.value;

      formData.append('username', username !== null  && username !== undefined ? username : "");
      formData.append('password', password !== null  && password !== undefined ? password : "");

      this.authService.getAccessToken(formData, this.error);
    }
  }

  constructor(
    public authService: AuthService,
    public route: Router,
    private titleService: Title
  ) { 
    this.titleService.setTitle("Вход в аккаунт")
  }

  form = new FormGroup({
    username: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required]),
  });

  ngOnInit(): void {
  }
}