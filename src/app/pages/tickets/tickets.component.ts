import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { ApiService } from '../../core/services/api.service';
import { Ticket, TicketPayload } from '../../models';

@Component({
  selector: 'app-tickets',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './tickets.component.html',
  styleUrl: './tickets.css',
})
export class TicketsComponent {
  ticketForm = {
    race_id: 1,
    ticket_holder_name: '',
    seat_category: 'Grandstand',
    quantity: 1,
    notes: '',
  };
  tickets: Ticket[] = [];
  error = '';
  success = '';
  selectedTicketId: number | null = null;

  constructor(private api: ApiService) {}

  loadTickets(): void {
    this.error = '';
    this.success = '';
    this.api.getTickets().subscribe({
      next: (data) => {
        this.tickets = data;
      },
      error: () => {
        this.error = 'Failed to load tickets. Please login first.';
      },
    });
  }

  submitTicket(): void {
    this.error = '';
    this.success = '';
    const payload: TicketPayload = { ...this.ticketForm };

    const request = this.selectedTicketId
      ? this.api.updateTicket(this.selectedTicketId, payload)
      : this.api.createTicket(payload);

    request.subscribe({
      next: () => {
        this.success = this.selectedTicketId
          ? 'Ticket updated successfully.'
          : 'Ticket purchased successfully.';
        this.resetForm();
        this.loadTickets();
      },
      error: () => {
        this.error = 'Ticket request failed. Check login and field values.';
      },
    });
  }

  editTicket(ticket: Ticket): void {
    this.selectedTicketId = ticket.id;
    this.ticketForm = {
      race_id: ticket.race_detail.id,
      ticket_holder_name: ticket.ticket_holder_name,
      seat_category: ticket.seat_category,
      quantity: ticket.quantity,
      notes: ticket.notes,
    };
    this.success = '';
    this.error = '';
  }

  deleteTicket(id: number): void {
    this.error = '';
    this.success = '';
    this.api.deleteTicket(id).subscribe({
      next: () => {
        this.success = 'Ticket deleted successfully.';
        this.loadTickets();
      },
      error: () => {
        this.error = 'Failed to delete ticket.';
      },
    });
  }

  resetForm(): void {
    this.selectedTicketId = null;
    this.ticketForm = {
      race_id: 1,
      ticket_holder_name: '',
      seat_category: 'Grandstand',
      quantity: 1,
      notes: '',
    };
  }
}
