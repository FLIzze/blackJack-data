import Head from "next/head";
import { Case } from "@/components";
import { faFile,faWineBottle, faHeartCrack, faRightFromBracket } from '@fortawesome/free-solid-svg-icons';
import axios from "axios";
import useSWR from "swr";
import { Stats } from "@/types/types";
import config from "@/../config.json";
import Tab from "@/components/Tab";

const fetcher = (url: string) => axios.get(url).then((res) => res.data)

export default function Home(props: Readonly<{ api: string }>) {
  const Icons = [faFile, faHeartCrack, faHeartCrack, faRightFromBracket, faRightFromBracket, faWineBottle, faWineBottle]

  const { data: stats, error } = useSWR(`${props.api}/total_games`, fetcher)
  const { data: games, error: errGame } = useSWR(`${props.api}/best_choice`, fetcher)
  if (!stats || !games) return <div>Loading...</div>
  if (error || errGame) return <div>Error...</div>

  return (
    <>
      <Head>
        <title>Blackjack Analyzer</title>
        <meta name="description" content="Blackjack Analyzer" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <main className="container">
        <h1 className="title">Blackjack Analyzer</h1>

        <div className="stats">
          {
            Object.keys(stats.total_games).map((key, index) => {
              return (
                <Case key={index + key} icon={Icons[index]} title={config.titles[index]} value={stats.total_games[key as keyof Stats].toString()} />
              )
            })
          }
        </div>

        <div className="charts">
          <Tab datas={games.best_choice} api={props.api} />
        </div>
      </main>
    </>
  );
}

export const getServerSideProps = async () => {
  const api = process.env.API_URL;

  return {
    props: {
      api,
    },
  };
}
