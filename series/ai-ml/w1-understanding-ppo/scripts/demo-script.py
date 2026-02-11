#!/usr/bin/env python3
"""
Demo Script for PPO Workshop
This script demonstrates all key concepts live during the workshop
"""

import gymnasium as gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import time

print("=" * 70)
print("PPO WORKSHOP - LIVE DEMONSTRATIONS")
print("=" * 70)
print()

# ============================================================================
# DEMO 1: Shared Kernel Concept (Using Lunar Lander Environment)
# ============================================================================

def demo1_environment_basics():
    """
    Demonstrate the basics of the Lunar Lander environment
    Similar to how we showed shared kernel in container workshop
    """
    print("\n" + "=" * 70)
    print("DEMO 1: Understanding the Lunar Lander Environment")
    print("=" * 70)
    
    env = gym.make('LunarLander-v2')
    
    print("\n📊 Environment Specifications:")
    print(f"  State space: {env.observation_space} (8 dimensions)")
    print(f"  Action space: {env.action_space} (4 discrete actions)")
    print()
    print("  State components:")
    print("    [0] x position")
    print("    [1] y position")
    print("    [2] x velocity")
    print("    [3] y velocity")
    print("    [4] angle")
    print("    [5] angular velocity")
    print("    [6] left leg contact (0 or 1)")
    print("    [7] right leg contact (0 or 1)")
    print()
    print("  Actions:")
    print("    0: Do nothing")
    print("    1: Fire left engine")
    print("    2: Fire main engine")
    print("    3: Fire right engine")
    
    print("\n🎮 Running random policy for 5 steps...")
    state, _ = env.reset(seed=42)
    print(f"\nInitial state:")
    print(f"  Position: ({state[0]:.3f}, {state[1]:.3f})")
    print(f"  Velocity: ({state[2]:.3f}, {state[3]:.3f})")
    
    for step in range(5):
        action = env.action_space.sample()
        next_state, reward, terminated, truncated, info = env.step(action)
        
        action_names = ['Do nothing', 'Fire left', 'Fire main', 'Fire right']
        print(f"\n  Step {step + 1}:")
        print(f"    Action: {action_names[action]}")
        print(f"    Reward: {reward:.3f}")
        print(f"    New position: ({next_state[0]:.3f}, {next_state[1]:.3f})")
        
        if terminated or truncated:
            print("    Episode ended!")
            break
        
        state = next_state
    
    env.close()
    print("\n✓ Demo 1 complete!")
    input("Press Enter to continue to Demo 2...")


# ============================================================================
# DEMO 2: Neural Network Architecture
# ============================================================================

def demo2_network_architecture():
    """
    Demonstrate the Actor-Critic network architecture
    """
    print("\n" + "=" * 70)
    print("DEMO 2: Actor-Critic Network Architecture")
    print("=" * 70)
    
    class ActorCritic(nn.Module):
        def __init__(self, state_dim, action_dim, hidden_dim=64):
            super(ActorCritic, self).__init__()
            self.shared = nn.Sequential(
                nn.Linear(state_dim, hidden_dim),
                nn.ReLU(),
                nn.Linear(hidden_dim, hidden_dim),
                nn.ReLU()
            )
            self.actor = nn.Linear(hidden_dim, action_dim)
            self.critic = nn.Linear(hidden_dim, 1)
        
        def forward(self, state):
            features = self.shared(state)
            action_logits = self.actor(features)
            state_value = self.critic(features)
            return action_logits, state_value
    
    # Create network
    network = ActorCritic(state_dim=8, action_dim=4)
    
    print("\n🧠 Network Structure:")
    print(network)
    
    # Count parameters
    total_params = sum(p.numel() for p in network.parameters())
    print(f"\n📊 Total parameters: {total_params:,}")
    
    # Test with dummy input
    print("\n🔬 Testing network with dummy state...")
    dummy_state = torch.randn(1, 8)
    print(f"Input state shape: {dummy_state.shape}")
    print(f"Input state values: {dummy_state[0].numpy()}")
    
    action_logits, state_value = network(dummy_state)
    action_probs = F.softmax(action_logits, dim=-1)
    
    print(f"\nOutput:")
    print(f"  Action logits: {action_logits[0].detach().numpy()}")
    print(f"  Action probabilities: {action_probs[0].detach().numpy()}")
    print(f"  State value: {state_value[0].item():.3f}")
    
    print("\n💡 Key insight: The network outputs both:")
    print("   - What to do (Actor: action probabilities)")
    print("   - How good is this state (Critic: value)")
    
    print("\n✓ Demo 2 complete!")
    input("Press Enter to continue to Demo 3...")


# ============================================================================
# DEMO 3: PPO Clipping Visualization
# ============================================================================

def demo3_ppo_clipping():
    """
    Demonstrate how PPO clipping works
    """
    print("\n" + "=" * 70)
    print("DEMO 3: PPO Clipping Mechanism")
    print("=" * 70)
    
    print("\n📐 PPO uses clipping to prevent large policy updates")
    print("   Formula: L = min(ratio * A, clip(ratio, 1-ε, 1+ε) * A)")
    print()
    
    clip_epsilon = 0.2
    
    # Example scenarios
    scenarios = [
        ("Good action (A > 0), policy makes it more likely", 1.5, 2.0),
        ("Good action (A > 0), policy makes it less likely", 1.5, 0.7),
        ("Bad action (A < 0), policy makes it less likely", -1.5, 0.7),
        ("Bad action (A < 0), policy makes it more likely", -1.5, 1.5),
    ]
    
    print(f"Clip range: [{1 - clip_epsilon}, {1 + clip_epsilon}] = [0.8, 1.2]")
    print()
    
    for desc, advantage, ratio in scenarios:
        # Unclipped objective
        surr1 = ratio * advantage
        
        # Clipped objective
        ratio_clipped = np.clip(ratio, 1 - clip_epsilon, 1 + clip_epsilon)
        surr2 = ratio_clipped * advantage
        
        # PPO objective (take min)
        ppo_objective = min(surr1, surr2)
        
        print(f"Scenario: {desc}")
        print(f"  Advantage: {advantage:+.2f}")
        print(f"  Ratio (π_new / π_old): {ratio:.2f}")
        print(f"  Unclipped objective: {surr1:+.3f}")
        print(f"  Clipped objective: {surr2:+.3f}")
        print(f"  PPO objective (min): {ppo_objective:+.3f}")
        
        if ratio_clipped != ratio:
            print(f"  ⚠️  Clipping activated! Ratio clipped to {ratio_clipped:.2f}")
        else:
            print(f"  ✓ No clipping needed")
        print()
    
    print("💡 Key insight: Clipping prevents the policy from changing too much")
    print("   - If making good actions more likely: clip to +20% increase")
    print("   - If making bad actions less likely: clip to -20% decrease")
    
    print("\n✓ Demo 3 complete!")
    input("Press Enter to continue to Demo 4...")


# ============================================================================
# DEMO 4: Advantage Estimation
# ============================================================================

def demo4_advantage_estimation():
    """
    Demonstrate how advantages are computed
    """
    print("\n" + "=" * 70)
    print("DEMO 4: Advantage Estimation (GAE)")
    print("=" * 70)
    
    print("\n📊 Advantages tell us: 'How much better was this action vs average?'")
    print()
    
    # Example trajectory
    rewards = np.array([1.0, 1.0, 1.0, 1.0, 10.0])
    values = np.array([5.0, 5.0, 5.0, 5.0, 0.0])
    dones = np.array([0, 0, 0, 0, 1])
    
    print("Example trajectory:")
    print(f"  Rewards: {rewards}")
    print(f"  Values:  {values}")
    print()
    
    gamma = 0.99
    lambda_ = 0.95
    
    # Compute GAE
    advantages = np.zeros_like(rewards)
    last_advantage = 0
    
    for t in reversed(range(len(rewards))):
        if t == len(rewards) - 1:
            next_value = 0
        else:
            next_value = values[t + 1]
        
        # TD error
        delta = rewards[t] + gamma * next_value * (1 - dones[t]) - values[t]
        
        # GAE
        advantages[t] = delta + gamma * lambda_ * (1 - dones[t]) * last_advantage
        last_advantage = advantages[t]
        
        if dones[t]:
            last_advantage = 0
    
    print(f"Computed advantages: {advantages}")
    print()
    
    # Interpretation
    for t in range(len(advantages)):
        if advantages[t] > 0:
            sentiment = "✓ Better than expected"
        else:
            sentiment = "✗ Worse than expected"
        print(f"  Step {t}: Advantage = {advantages[t]:+.3f} - {sentiment}")
    
    print("\n💡 Key insight: Positive advantage = reinforce this action")
    print("                Negative advantage = discourage this action")
    
    print("\n✓ Demo 4 complete!")
    input("Press Enter to continue to Demo 5...")


# ============================================================================
# DEMO 5: Random vs Trained Policy Comparison
# ============================================================================

def demo5_policy_comparison():
    """
    Compare random policy vs trained policy (if available)
    Note: This demo requires a pre-trained model
    """
    print("\n" + "=" * 70)
    print("DEMO 5: Random vs Trained Policy")
    print("=" * 70)
    
    print("\n[📹 INSTRUCTOR: Show pre-recorded GIF comparison here]")
    print()
    print("What you should observe:")
    print("  Random policy:")
    print("    - Erratic movements")
    print("    - Often crashes immediately")
    print("    - Average reward: ~-200")
    print()
    print("  Trained PPO policy:")
    print("    - Smooth, controlled descent")
    print("    - Adjusts to stay centered")
    print("    - Gentle landing")
    print("    - Average reward: ~250")
    print()
    
    # Try to load and run trained model if available
    model_path = "../demo-assets/ppo_trained.pth"
    
    print("💡 Key insight: PPO learns a smooth, optimal policy through")
    print("   trial and error, balancing exploration and exploitation")
    
    print("\n✓ Demo 5 complete!")
    input("Press Enter to continue to Demo 6...")


# ============================================================================
# DEMO 6: Training Dynamics
# ============================================================================

def demo6_training_dynamics():
    """
    Show what happens during training (metrics to watch)
    """
    print("\n" + "=" * 70)
    print("DEMO 6: What to Monitor During Training")
    print("=" * 70)
    
    print("\n📊 Key metrics to track:")
    print()
    
    metrics = {
        'Episode Reward': {
            'healthy': '+150 to +250 (successful landing)',
            'problem': 'Stuck at -200 (crashing)',
            'watch_for': 'Steady increase over time'
        },
        'Policy Ratio': {
            'healthy': 'Mean ~1.0, std ~0.1',
            'problem': 'Mean far from 1.0, many clipped',
            'watch_for': 'Most ratios in [0.9, 1.1]'
        },
        'Value Loss': {
            'healthy': 'Decreasing, then stabilizes',
            'problem': 'Increasing or oscillating wildly',
            'watch_for': 'Steady decrease'
        },
        'Entropy': {
            'healthy': 'High (>1.5) early, low (<0.5) late',
            'problem': 'Drops to 0 immediately',
            'watch_for': 'Gradual decrease'
        },
    }
    
    for metric, info in metrics.items():
        print(f"{metric}:")
        print(f"  ✓ Healthy: {info['healthy']}")
        print(f"  ✗ Problem: {info['problem']}")
        print(f"  👀 Watch for: {info['watch_for']}")
        print()
    
    print("💡 Key insight: Training RL is like teaching someone to drive")
    print("   - Early: Lots of exploration (high entropy), many mistakes")
    print("   - Middle: Learning what works (rewards increase)")
    print("   - Late: Confident, consistent performance (low entropy)")
    
    print("\n✓ Demo 6 complete!")
    print("\n" + "=" * 70)
    print("ALL DEMONSTRATIONS COMPLETE!")
    print("=" * 70)
    print()
    print("You're now ready for the hands-on exercises!")
    print("Navigate to the exercises/ directory and start with exercise1")


# ============================================================================
# Main Demo Runner
# ============================================================================

def main():
    """Run all demonstrations"""
    print("\nThis script will run 6 live demonstrations:")
    print("  1. Environment Basics")
    print("  2. Network Architecture")
    print("  3. PPO Clipping")
    print("  4. Advantage Estimation")
    print("  5. Policy Comparison")
    print("  6. Training Dynamics")
    print()
    
    try:
        demo1_environment_basics()
        demo2_network_architecture()
        demo3_ppo_clipping()
        demo4_advantage_estimation()
        demo5_policy_comparison()
        demo6_training_dynamics()
    except KeyboardInterrupt:
        print("\n\nDemonstration interrupted by user.")
    except Exception as e:
        print(f"\n\nError during demonstration: {e}")
        print("Please check your environment setup.")
    
    print("\nThank you for attending the PPO workshop! 🚀")


if __name__ == "__main__":
    main()
