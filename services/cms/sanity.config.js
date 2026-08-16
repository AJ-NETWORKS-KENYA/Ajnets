/**
 * Sanity Studio Configuration for AJNETWORKS
 */
import { defineConfig } from 'sanity';
import { deskTool } from 'sanity/desk';
import { schemaTypes } from './schemas/schema';

export default defineConfig({
  name: 'ajnetworks-studio',
  title: 'AJNETWORKS Content Studio',

  projectId: process.env.SANITY_PROJECT_ID || 'your_project_id',
  dataset: process.env.SANITY_DATASET || 'production',

  plugins: [
    deskTool({
      structure: (S) =>
        S.list()
          .title('Content Hub')
          .items([
            S.listItem()
              .title('Tech Insights & Articles')
              .schemaType('post')
              .child(S.documentTypeList('post').title('Published Articles')),
            S.listItem()
              .title('Client Case Studies')
              .schemaType('caseStudy')
              .child(S.documentTypeList('caseStudy').title('Case Studies')),
            S.listItem()
              .title('Practice Areas & Services')
              .schemaType('service')
              .child(S.documentTypeList('service').title('Services')),
            S.listItem()
              .title('Consultants & Authors')
              .schemaType('teamMember')
              .child(S.documentTypeList('teamMember').title('Team Members')),
            S.divider(),
            S.listItem()
              .title('Global Site Settings')
              .child(
                S.editor()
                  .schemaType('siteSettings')
                  .documentId('siteSettings')
              ),
          ]),
    }),
  ],

  schema: {
    types: schemaTypes,
  },
});
