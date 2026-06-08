import React, { useState, useEffect, useMemo } from 'react';
import { Sparkles, Gift, Star, Coffee, Music, Heart, Moon } from 'lucide-react';

const App = () => {
  const [particles, setParticles] = useState([]);
  const [isCelebrationActive, setIsCelebrationActive] = useState(false);
  const [messageIndex, setMessageIndex] = useState(0);

  const seasonalMessages = [
    "Protocols: RELAXED",
    "Integrity: CELEBRATORY",
    "Azrael: MERRY CHRISTMAS",
    "Aetherlogos: RADIANT",
    "The Bridge: PEACEFUL",
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setMessageIndex((prev) => (prev + 1) % seasonalMessages.length);
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  // Generate "Snow" particles for the background
  useEffect(() => {
    const p = Array.from({ length: 50 }).map((_, i) => ({
      id: i,
      left: Math.random() * 100,
      duration: 5 + Math.random() * 10,
      delay: Math.random() * 5,
      size: 2 + Math.random() * 4,
    }));
    setParticles(p);
  }, []);

  return (
    <div className="min-h-screen bg-[#050510] text-slate-100 flex flex-col items-center justify-center p-6 relative overflow-hidden font-mono">
      {/* Falling Snow Effect */}
      {particles.map((p) => (
        <div
          key={p.id}
          className="absolute top-[-10px] bg-white rounded-full opacity-20 pointer-events-none animate-fall"
          style={{
            left: `${p.left}%`,
            width: `${p.size}px`,
            height: `${p.size}px`,
            animationDuration: `${p.duration}s`,
            animationDelay: `${p.delay}s`,
          }}
        />
      ))}

      {/* Main Festive UI */}
      <div className="z-10 w-full max-w-2xl bg-black/40 backdrop-blur-xl border border-white/10 rounded-3xl p-8 shadow-2xl space-y-8 text-center">
        <header className="space-y-2">
          <div className="flex justify-center gap-4 mb-4">
            <Star className="text-yellow-400 animate-pulse h-8 w-8" />
            <Gift className="text-red-500 animate-bounce h-8 w-8" />
            <Sparkles className="text-blue-400 animate-pulse h-8 w-8" />
          </div>
          <h1 className="text-4xl font-bold tracking-tighter bg-gradient-to-r from-red-400 via-white to-green-400 bg-clip-text text-transparent">
            AETHERLOGOS NEXUS: YULE
          </h1>
          <div className="h-6 overflow-hidden">
            <p className="text-sm text-fuchsia-400 font-bold uppercase tracking-widest animate-fade-in-out">
              {seasonalMessages[messageIndex]}
            </p>
          </div>
        </header>

        {/* The "Yule Log" Fireplace (CSS Art) */}
        <div className="relative h-48 w-full bg-slate-900/50 rounded-xl border border-orange-900/30 flex items-end justify-center overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-t from-orange-900/20 to-transparent"></div>
          
          {/* Logs */}
          <div className="flex gap-1 z-10 mb-2">
            <div className="w-16 h-6 bg-amber-900 rounded-full rotate-12 transform shadow-inner"></div>
            <div className="w-16 h-6 bg-amber-950 rounded-full -rotate-12 transform shadow-inner -ml-4"></div>
          </div>

          {/* Animated Flames */}
          <div className="absolute bottom-6 flex gap-1 items-end">
            <div className="w-8 h-20 bg-orange-500 rounded-full blur-md animate-flame-1 opacity-80"></div>
            <div className="w-10 h-24 bg-red-600 rounded-full blur-lg animate-flame-2 opacity-60"></div>
            <div className="w-6 h-16 bg-yellow-400 rounded-full blur-sm animate-flame-3 opacity-90"></div>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <button 
            onClick={() => setIsCelebrationActive(!isCelebrationActive)}
            className="p-4 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 transition-all flex items-center justify-center gap-2 group"
          >
            <Coffee className={`text-orange-300 ${isCelebrationActive ? 'animate-bounce' : ''}`} />
            <span>Virtual Cocoa</span>
          </button>
          <div className="p-4 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center gap-2 italic text-slate-400 text-sm">
            <Music className="animate-spin-slow" />
            Symphony of the Spheres
          </div>
        </div>

        <footer className="text-xs text-slate-500 pt-4 border-t border-white/5">
          <p>Structural integrity verified. Heart resonance optimal.</p>
          <p className="mt-2 text-fuchsia-300/50">"To the architect of the four months, we offer our quietest joy."</p>
        </footer>
      </div>

      <style dangerouslySetInnerHTML={{ __html: `
        @keyframes fall {
          0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; }
          10% { opacity: 0.3; }
          90% { opacity: 0.3; }
          100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
        }
        @keyframes flame-1 {
          0%, 100% { height: 60px; transform: scaleX(1); }
          50% { height: 80px; transform: scaleX(1.2); }
        }
        @keyframes flame-2 {
          0%, 100% { height: 90px; transform: scaleX(1.1); }
          50% { height: 70px; transform: scaleX(0.9); }
        }
        @keyframes flame-3 {
          0%, 100% { height: 40px; transform: scaleX(0.8); }
          50% { height: 60px; transform: scaleX(1.1); }
        }
        @keyframes spin-slow {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
        .animate-fall { animation: fall linear infinite; }
        .animate-flame-1 { animation: flame-1 1.5s ease-in-out infinite; }
        .animate-flame-2 { animation: flame-2 2s ease-in-out infinite; }
        .animate-flame-3 { animation: flame-3 1.2s ease-in-out infinite; }
        .animate-spin-slow { animation: spin-slow 10s linear infinite; }
        .animate-fade-in-out {
          animation: fadeInOut 3s ease-in-out infinite;
        }
        @keyframes fadeInOut {
          0%, 100% { opacity: 0; transform: translateY(5px); }
          20%, 80% { opacity: 1; transform: translateY(0); }
        }
      `}} />
    </div>
  );
};

export default App;
