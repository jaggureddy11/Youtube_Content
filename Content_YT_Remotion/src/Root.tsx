import "./index.css";
import { Composition } from "remotion";
import { HashMapExplainer } from "./HashMapExplainer";
import { RecursionExplainer } from "./RecursionExplainer";

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
      <Composition
        id="RecursionExplainer"
        component={RecursionExplainer}
        durationInFrames={1170}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
