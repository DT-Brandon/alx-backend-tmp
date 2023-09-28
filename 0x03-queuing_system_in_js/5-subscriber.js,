import redis from 'redis';

const cli = redis.createClient();

cli.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

cli.on('connect', () => {
  console.log('Redis client connected to the server');
});

const CHANNEL = 'holberton school channel';

cli.subscribe(CHANNEL);

cli.on('message', (channel, message) => {
  if (channel === CHANNEL) console.log(message);
  if (message === 'KILL_SERVER') {
    cli.unsubscribe(CHANNEL);
    cli.quit();
  }
});
