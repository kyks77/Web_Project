export interface Race {
  id: number;
  grand_prix_name: string;
  location: string;
  race_date: string;
  circuit_name: string;
  winner_driver: number | null;
  winner_driver_name: string | null;
  laps: number;
}
