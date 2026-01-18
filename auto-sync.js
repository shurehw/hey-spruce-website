#!/usr/bin/env node

/**
 * Auto-sync script for Happy integration
 * Watches for changes and auto-commits/pushes to GitHub
 * Run: node auto-sync.js
 */

const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

const SYNC_INTERVAL = 5 * 60 * 1000; // 5 minutes
const PROJECT_DIR = 'c:\\Users\\JacobShure\\groundops website';
const DEV_BRANCH = 'dev'; // Mobile coding happens on dev branch

console.log('🔄 Happy Auto-Sync started');
console.log(`📁 Watching: ${PROJECT_DIR}`);
console.log(`🌿 Branch: ${DEV_BRANCH} (mobile coding branch)`);
console.log(`⏱️  Sync interval: ${SYNC_INTERVAL / 1000}s`);
console.log(`📦 Production (master) won't auto-deploy from mobile edits\n`);

function runCommand(command) {
  return new Promise((resolve, reject) => {
    exec(command, { cwd: PROJECT_DIR }, (error, stdout, stderr) => {
      if (error) {
        reject(error);
      } else {
        resolve(stdout.trim());
      }
    });
  });
}

async function checkAndSync() {
  try {
    console.log(`[${new Date().toLocaleTimeString()}] Checking for changes...`);

    // Ensure we're on dev branch
    const currentBranch = await runCommand('git branch --show-current');
    if (currentBranch !== DEV_BRANCH) {
      console.log(`⚠️  Switching to ${DEV_BRANCH} branch...`);
      await runCommand(`git checkout ${DEV_BRANCH}`);
    }

    // Pull latest changes first
    try {
      const pullOutput = await runCommand('git pull --rebase --autostash');
      if (!pullOutput.includes('Already up to date')) {
        console.log('📥 Pulled changes from GitHub');
      }
    } catch (error) {
      console.log('⚠️  Pull failed (might have conflicts):', error.message);
    }

    // Check for local changes
    const status = await runCommand('git status --porcelain');

    if (status) {
      console.log('📝 Found local changes, committing...');

      // Add all changes
      await runCommand('git add -A');

      // Commit with timestamp
      const timestamp = new Date().toISOString();
      const commitMsg = `Auto-sync: ${timestamp}\n\n🤖 Auto-synced for Happy mobile coding`;
      await runCommand(`git commit -m "${commitMsg}"`);

      // Push to remote
      await runCommand('git push');
      console.log('✅ Pushed changes to GitHub\n');
    } else {
      console.log('✓ No changes to sync\n');
    }
  } catch (error) {
    console.error('❌ Sync error:', error.message, '\n');
  }
}

// Initial sync
checkAndSync();

// Set up periodic sync
setInterval(checkAndSync, SYNC_INTERVAL);

console.log('👀 Watching for changes...\n');
console.log('💡 Tip: Make changes in VS Code or Happy app, they will auto-sync!');
console.log('Press Ctrl+C to stop\n');
