import React from 'react';
import { IconDefinition } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import styles from './style.module.scss';

interface CaseProps {
  icon?: IconDefinition;
  title: string;
  value: string;
}

const Case = ({
  icon,
  title,
  value,
}: CaseProps) => {
  return (
    <div className={styles.Case_container}>
      {icon && (
        <div className={styles.Case_icon}>
          <FontAwesomeIcon icon={icon} />
        </div>
      )}

      <div className={styles.Case_content}>
        <h2 className={styles.Case_title}>{title}</h2>
        <h2 className={styles.Case_value}>{value}</h2>
      </div>
    </div>
  );
};

export default Case;
