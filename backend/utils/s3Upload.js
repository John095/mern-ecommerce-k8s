import { S3Client } from '@aws-sdk/client-s3';
import multer from 'multer';
import multerS3 from 'multer-s3';

// Check if S3 is configured
const isS3Configured = () => {
  return process.env.AWS_ACCESS_KEY_ID && 
         process.env.AWS_SECRET_ACCESS_KEY && 
         process.env.S3_BUCKET_NAME;
};

// S3 Client setup
let s3;
if (isS3Configured()) {
  s3 = new S3Client({
    region: process.env.AWS_REGION || 'us-east-1',
    credentials: {
      accessKeyId: process.env.AWS_ACCESS_KEY_ID,
      secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
    },
  });
}

// Local storage setup
const localStorage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads');
  },
  filename: (req, file, cb) => {
    cb(null, `${file.fieldname}-${Date.now()}-${file.originalname}`);
  }
});

// S3 storage setup
const s3Storage = multerS3({
  s3: s3,
  bucket: process.env.S3_BUCKET_NAME,
  key: function (req, file, cb) {
    cb(null, `products/${Date.now()}-${file.originalname}`);
  },
  contentType: multerS3.AUTO_CONTENT_TYPE,
});

// File filter
const fileFilter = (req, file, cb) => {
  if (
    file.mimetype === 'image/png' ||
    file.mimetype === 'image/jpg' ||
    file.mimetype === 'image/jpeg'
  ) {
    cb(null, true);
  } else {
    cb(new Error('Images only!'));
  }
};

// Export upload middleware
export const upload = multer({
  storage: isS3Configured() ? s3Storage : localStorage,
  fileFilter,
}).single('image');

export { isS3Configured };