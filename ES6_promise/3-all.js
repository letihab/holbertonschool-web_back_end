import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  // Use Promise.all to collectively resolve all promises
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      // Extracting the resolved values from the promises
      const [photoResponse, userResponse] = results;
      console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
