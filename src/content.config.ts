import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const pageBaseSchema = z.object({
  slug: z.string(),
  title: z.string().min(10),
  description: z.string().min(30),
  keywords: z.string().optional(),
  canonicalUrl: z.string().url(),
  ogType: z.enum(['website', 'article']).default('website'),
  ogImage: z.string().url().default('https://ajnetworks.co/images/og-home.webp'),
  preloadImage: z.string().optional(),
  extraJsonLd: z.array(z.string()).default([]),
  extraHeadStyles: z.array(z.string()).default([]),
  extraFooterScripts: z.array(z.string()).default([]),
  showRwandaBanner: z.boolean().default(false),
  wrapInSiteDiv: z.boolean().default(true),
  bodyHtml: z.string().min(1),
});

const caseStudies = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/caseStudies' }),
  schema: pageBaseSchema.extend({
    client: z.string().optional(),
    industry: z.string().optional(),
    technologies: z.string().optional(),
    timeline: z.string().optional(),
    badges: z.array(z.string()).default([]),
  }),
});

const services = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/services' }),
  schema: pageBaseSchema.extend({
    heroTitle: z.string().optional(),
    heroSubtitle: z.string().optional(),
  }),
});

const company = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/company' }),
  schema: pageBaseSchema,
});

const insights = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/insights' }),
  schema: pageBaseSchema,
});

const system = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/system' }),
  schema: pageBaseSchema,
});

export const collections = {
  caseStudies,
  services,
  company,
  insights,
  system,
};
