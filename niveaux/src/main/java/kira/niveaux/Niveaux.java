package kira.niveaux;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document
public class Niveaux {
    @Id
    private String id;
    private int niveau;
    private String competenceId;
    private String utilisateurId;
}
