import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DriverStats, RaceSummary } from '../../models';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {
  summary: RaceSummary[] = [];
  stats: DriverStats[] = [];
  error = '';

  constructor(private api: ApiService) {}

  loadSummary(): void {
    this.error = '';
    this.api.getRaceSummary(true).subscribe({
      next: (data) => {
        this.summary = data;
      },
      error: () => {
        this.error = 'Failed to load race summary.';
      },
    });
  }

  loadStats(): void {
    this.error = '';
    this.api.getDriverStats().subscribe({
      next: (data) => {
        this.stats = data;
      },
      error: () => {
        this.error = 'Failed to load driver stats.';
      },
    });
  }
}
