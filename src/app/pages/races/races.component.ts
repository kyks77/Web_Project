import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

import { ApiService } from '../../core/services/api.service';
import { Race } from '../../models';

@Component({
  selector: 'app-races',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './races.component.html',
  styleUrl: './races.css',
})
export class RacesComponent {
  races: Race[] = [];
  error = '';

  constructor(private api: ApiService) {}

  loadRaces(): void {
    this.error = '';
    this.api.getRaces().subscribe({
      next: (data) => {
        this.races = data;
      },
      error: () => {
        this.error = 'Failed to load races.';
      },
    });
  }

  loadUpcomingRaces(): void {
    this.error = '';
    this.api.getRaces(true).subscribe({
      next: (data) => {
        this.races = data;
      },
      error: () => {
        this.error = 'Failed to load upcoming races.';
      },
    });
  }
}
