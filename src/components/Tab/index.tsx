import React from 'react';
import getInfosHand from '@/functions/Hands';

import styles from './style.module.scss';

type BlackjackData = {
  DealerHand: string;
  PlayerCard1: string;
  PlayerCard2: string;
  PlayerChoices: string;
};

type StrategyTable = { [key: string]: { [key: string]: string } };

const generateBlackjackStrategyTable = (data: BlackjackData[]): StrategyTable => {
    const table: StrategyTable = {};

    // Initialisation of the table
    const dealerHands = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'];
    const playerHands = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', '2-2', '3-3', '4-4', '5-5', '6-6', '7-7', '8-8', '9-9', '10-10', 'A-A'];
    dealerHands.forEach(dealerHand => {
        table[dealerHand] = {};
        playerHands.forEach(playerHand => {
            table[dealerHand][playerHand] = '-';
        });
    });

    // Fill the table with the data
    data.forEach(item => {
        const { DealerHand, PlayerCard1, PlayerCard2, PlayerChoices } = item;
        const playerHandsToCheck = [PlayerCard1, PlayerCard2];
        playerHandsToCheck.forEach(playerHand => {
            if (playerHand === 'A' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8');
            } else if (playerHand === '2' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('2-2');
            } else if (playerHand === '3' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('3-3');
            } else if (playerHand === '4' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('4-4');
            } else if (playerHand === '5' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('5-5');
            } else if (playerHand === '6' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('6-6');
            } else if (playerHand === '7' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('7-7');
            } else if (playerHand === '8' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('8-8');
            } else if (playerHand === '9' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('9-9');
            } else if (playerHand === '10' && (PlayerCard1 !== PlayerCard2)) {
                playerHandsToCheck.push('10-10');
            } else if (playerHand === 'A' && (PlayerCard1 === PlayerCard2)) {
                playerHandsToCheck.push('A-A');
            }

            playerHandsToCheck.forEach(hand => {
                table[DealerHand][hand] = PlayerChoices;
            });
        });
    });

    return table;
};

interface TabProps {
  datas: BlackjackData[];
  api: string;
}

const Tab = ({
  datas,
  api,
}: TabProps) => {
  const strategyTable = generateBlackjackStrategyTable(datas);

  const [handInfos, setHandInfos] = React.useState({} as any);

  const handleGetInfosHand = async (card1: string, card2: string, dealerHand: string) => {
    const hand = await getInfosHand(card1, card2, dealerHand, api);
    setHandInfos(hand);
  }
  return (
    <>
      {(handInfos && handInfos.double) && (
        <div className={styles.HandInfos}>
          <h2>Hand Infos</h2>
          <div>
            {Object.keys(handInfos).map((key, index) => (
              <div key={index}>
                <h3>{key}</h3>
                {Object.keys(handInfos[key]).map((key2, index2) => (
                  <p
                    key={index2}
                    style={{
                      color: handInfos[key][key2] > 70 ? 'var(--green)' : handInfos[key][key2] > 50 ? 'var(--yellow)' : 'var(--red)',
                    }}
                  >
                    {key2}: {handInfos[key][key2]} %
                  </p>
                ))}
                </div>
            ))}
            </div>
        </div>
      )}
    <div className={styles.Tab_container}>
      {strategyTable && (
        <table onMouseLeave={() => setHandInfos({})}>
          <thead>
            <tr>
                <th></th>
                {['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'].map(dealerHand => (
                    <th key={dealerHand}>{dealerHand}</th>
                ))}
            </tr>
          </thead>
          <tbody>
            {['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', '2-2', '3-3', '4-4', '5-5', '6-6', '7-7', '8-8', '9-9', '10-10', 'A-A'].map((playerHand, indexPlayer) => (
              <tr key={playerHand}>
                <td>{playerHand}</td>
                {['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'].map((dealerHand, index) => (
                  <td
                    key={dealerHand}
                    className={styles.Cell}
                    style={{
                      backgroundColor: strategyTable[dealerHand][playerHand] === 'hit' ? 'var(--red)' : strategyTable[dealerHand][playerHand] === 'stay' ? 'var(--yellow)' : strategyTable[dealerHand][playerHand] === 'split' ? 'var(--green)' : strategyTable[dealerHand][playerHand] === 'double' ? 'var(--blue)' : strategyTable[dealerHand][playerHand] === 'double_after_split' ? 'yellow' : strategyTable[dealerHand][playerHand] === 'surrender' ? 'var(--purple)' : strategyTable[dealerHand][playerHand] === 'blackjack' ? 'var(--cyan)' : 'var(--color-dark',
                      borderRadius: (index === 0 && indexPlayer === 0) ? '8px 0 0 0' : (index === 9 && indexPlayer === 0) ? '0 8px 0 0' : (index === 0 && indexPlayer === 26) ? '0 0 0 8px' : '0',
                    }}
                    onMouseEnter={() => handleGetInfosHand(playerHand.split('-')[0], playerHand.split('-')[1], dealerHand)}
                  >
                    {strategyTable[dealerHand][playerHand]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
    </>
  );
};

export default Tab;
