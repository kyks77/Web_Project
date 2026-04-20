import { Routes } from '@angular/router';

import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { RacesComponent } from './pages/races/races.component';
import { TeamsComponent } from './pages/teams/teams.component';
import { TicketsComponent } from './pages/tickets/tickets.component';

export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'home' },
  { path: 'home', component: HomeComponent },
  { path: 'teams', component: TeamsComponent },
  { path: 'races', component: RacesComponent },
  { path: 'tickets', component: TicketsComponent },
  { path: 'login', component: LoginComponent },
  { path: '**', redirectTo: 'home' },
];
