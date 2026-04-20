import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

import { ApiService } from '../../core/services/api.service';
import { Team } from '../../models';

@Component({
  selector: 'app-teams',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './teams.component.html',
  styleUrl: './teams.css',
})
export class TeamsComponent {
  teams: Team[] = [];
  error = '';

  constructor(private api: ApiService) {}

  loadTeams(): void {
    this.error = '';
    this.api.getTeams().subscribe({
      next: (data) => {
        this.teams = data;
      },
      error: () => {
        this.error = 'Failed to load teams.';
      },
    });
  }
}
