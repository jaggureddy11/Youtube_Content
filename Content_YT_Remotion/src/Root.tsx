import "./index.css";
import { Composition } from "remotion";
import { HashMapExplainer } from "./HashMapExplainer";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="HashMapExplainer"
        component={HashMapExplainer}
        durationInFrames={780}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
