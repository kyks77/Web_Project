import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { catchError, map, Observable, of, tap } from 'rxjs';

import { ApiService } from './api.service';

@Injectable({ providedIn: 'root' })
export class AuthService {
  constructor(
    private api: ApiService,
    private router: Router,
  ) {}

  login(data: { username: string; password: string }) {
    return this.api.login(data).pipe(
      tap((res) => {
        this.setStorageItem('access_token', res.access);
        this.setStorageItem('refresh_token', res.refresh);
        this.setStorageItem('username', res.username);
      }),
    );
  }

  logout(): Observable<boolean> {
    const refresh = this.getStorageItem('refresh_token');

    if (!refresh) {
      this.clearSession();
      return of(true);
    }

    return this.api.logout(refresh).pipe(
      map(() => true),
      catchError(() => of(false)),
      tap(() => {
        this.clearSession();
        void this.router.navigate(['/login']);
      }),
    );
  }

  clearSession(): void {
    this.removeStorageItem('access_token');
    this.removeStorageItem('refresh_token');
    this.removeStorageItem('username');
  }

  getUsername(): string {
    return this.getStorageItem('username') ?? 'Guest';
  }

  isLoggedIn(): boolean {
    return !!this.getStorageItem('access_token');
  }

  private getStorageItem(key: string): string | null {
    return typeof localStorage !== 'undefined' ? localStorage.getItem(key) : null;
  }

  private setStorageItem(key: string, value: string): void {
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem(key, value);
    }
  }

  private removeStorageItem(key: string): void {
    if (typeof localStorage !== 'undefined') {
      localStorage.removeItem(key);
    }
  }
}
