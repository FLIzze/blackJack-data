export type Stats = {
  total_games: number;
  total_loss_rate: number;
  total_losses: number;
  total_push_rate: number;
  total_pushes: number;
  total_win_rate: number;
  total_wins: number;
};

export type GameData = {
  DealerHand: string;
  LossRate: number;
  Lost: string;
  PlayerCard1: string;
  PlayerCard2: string;
  PlayerChoices: string;
  Push: string;
  PushRate: number;
  Total: string;
  Win: string;
  WinRate: number;
};
