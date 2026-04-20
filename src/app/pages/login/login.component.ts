import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.css',
})
export class LoginComponent {
  loginForm = {
    username: '',
    password: '',
  };
  error = '';
  success = '';

  constructor(
    private auth: AuthService,
    private router: Router,
  ) {}

  login(): void {
    this.error = '';
    this.success = '';
    this.auth.login(this.loginForm).subscribe({
      next: () => {
        this.success = 'Login successful.';
        void this.router.navigate(['/tickets']);
      },
      error: () => {
        this.error = 'Login failed. Check username and password.';
      },
    });
  }
}
