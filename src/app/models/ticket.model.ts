import { Race } from './race.model';

export interface Ticket {
  id: number;
  user_username: string;
  race_detail: Race;
  ticket_holder_name: string;
  seat_category: string;
  quantity: number;
  notes: string;
  purchased_at: string;
}

export interface TicketPayload {
  race_id: number;
  ticket_holder_name: string;
  seat_category: string;
  quantity: number;
  notes: string;
}

export interface RaceSummary {
  grand_prix_name: string;
  race_date: string;
  location: string;
  circuit_name: string;
  winner_driver_name: string | null;
}
