import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import {
  AuthResponse,
  DriverStats,
  Race,
  RaceSummary,
  Team,
  Ticket,
  TicketPayload,
} from '../../models';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  login(data: { username: string; password: string }) {
    return this.http.post<AuthResponse>(`${this.baseUrl}/auth/login/`, data);
  }

  logout(refresh: string) {
    return this.http.post<{ detail: string }>(`${this.baseUrl}/auth/logout/`, { refresh });
  }

  getTeams() {
    return this.http.get<Team[]>(`${this.baseUrl}/teams/`);
  }

  getRaces(upcoming = false) {
    return this.http.get<Race[]>(
      `${this.baseUrl}/races/${upcoming ? '?upcoming=true' : ''}`,
    );
  }

  getRaceSummary(upcoming = true) {
    return this.http.get<RaceSummary[]>(
      `${this.baseUrl}/races/summary/?upcoming=${upcoming}`,
    );
  }

  getDriverStats() {
    return this.http.get<DriverStats[]>(`${this.baseUrl}/stats/drivers/`);
  }

  getTickets() {
    return this.http.get<Ticket[]>(`${this.baseUrl}/tickets/`);
  }

  createTicket(data: TicketPayload) {
    return this.http.post<Ticket>(`${this.baseUrl}/tickets/`, data);
  }

  updateTicket(id: number, data: TicketPayload) {
    return this.http.put<Ticket>(`${this.baseUrl}/tickets/${id}/`, data);
  }

  deleteTicket(id: number) {
    return this.http.delete<void>(`${this.baseUrl}/tickets/${id}/`);
  }
}
